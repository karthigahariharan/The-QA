const puppeteer = require("puppeteer");
const path = require("path");
const fs = require("fs");

const htmls = fs.readdirSync(path.join("factbook", "geos")).filter(f => f.endsWith("html"));


(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  for (let i = 0; i < htmls.length; i++) {
    const country = htmls[i].split(".")[0];
    await page.goto(`file:///C:/Users/aksha/Documents/Projects/prototypes/cia/factbook/geos/${country}.html`, { waitUntil: "networkidle2" });
    try {
      const html = await page.$eval("#countryInfo", e => e.outerHTML);
      const outputPath = path.join("rendered", `${country}.html`);
      fs.writeFileSync(outputPath, html, { encoding: "utf8" });
    } catch (error) {
      console.log(country);
      console.error(error);
    }
  }

  await browser.close();
})();
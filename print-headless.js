const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:8080/?print-pdf', { waitUntil: 'networkidle2' });
  await page.emulateMedia('screen');
  await page.pdf({
    path: 'slides.pdf',
    format: 'A4',
    landscape: true,
    printBackground: true,
    margin: 0,
    preferCSSPageSize: true,
    width: '297mm',
    height: '210mm',
  });

  await browser.close();
})();

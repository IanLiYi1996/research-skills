const pptxgen = require('pptxgenjs');
const html2pptx = require('./html2pptx');
const path = require('path');

async function createPresentation() {
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    pptx.title = 'DeepSeek V3.2';
    pptx.author = 'DeepSeek AI';
    pptx.subject = 'Efficient Reasoning & Agentic AI';

    const slidesDir = path.join(__dirname, 'slides');
    const slides = [
        'slide1-cover.html',
        'slide2-overview.html',
        'slide3-breakthroughs.html',
        'slide4-dsa.html',
        'slide5-rl.html',
        'slide6-agent.html',
        'slide7-variants.html',
        'slide8-usage.html'
    ];

    for (const slideFile of slides) {
        const htmlPath = path.join(slidesDir, slideFile);
        console.log(`Processing: ${slideFile}`);
        await html2pptx(htmlPath, pptx);
    }

    const outputPath = path.join(__dirname, 'DeepSeek-V3.2-Presentation.pptx');
    await pptx.writeFile({ fileName: outputPath });
    console.log(`Presentation saved to: ${outputPath}`);
}

createPresentation().catch(err => {
    console.error('Error:', err);
    process.exit(1);
});

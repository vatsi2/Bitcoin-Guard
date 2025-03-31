use printpdf::{PdfDocument, Mm};

fn generate_pdf_report(report: &str) -> Vec<u8> {
    let doc = PdfDocument::empty();
    let page = doc.add_page(Mm(210.0), Mm(297.0));
    doc.save_to_bytes().unwrap()
}

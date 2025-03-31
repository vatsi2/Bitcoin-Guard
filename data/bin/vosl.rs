use reqwest::blocking::get;

fn is_sanctioned(address: &str) -> bool {
    let response = get("https://api.treasury.gov/sdn")
        .unwrap()
        .text()
        .unwrap();
    response.contains(address)
}

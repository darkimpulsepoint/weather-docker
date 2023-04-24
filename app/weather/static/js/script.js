async function get_weather(){
    let select = document.getElementById("select-city")
    let url = "accuweather.com/" + select.options[select.selectedIndex].value
    let response = await fetch("api/weather?url=" + url);
    return await get_json_by_url("api/weather?url=" + url)

}

async function show_weather(){
    let weather = await get_weather()
    let info = document.getElementById("info")
    info.innerText=""
    for (let el in weather){
        let label = document.createElement("label")
        label.textContent=el + ": "

        let value = document.createElement("span")
        value.textContent=weather[el]

        info.append(label)
        info.append(value)
        info.append(document.createElement("br"))
    }
}

function clean_select_city_field(){
        document.getElementById("select-city").innerHTML = ""
}

async function get_json_by_url(url){
    let response = await fetch(url);
    let json_data
    if (response.ok) {
        json_data = await response.json();
    }
    return json_data
}

async function update_places() {
    clean_select_city_field()
    let url = "/api/places?city=" + document.getElementById("place").value
    let json_data = await get_json_by_url(url)
    let places = json_data["places"]
    let select_city = document.getElementById("select-city")

    for (let el in places) {
        select_city.append(new Option(el, places[el]))
    }
}
/* Web API */
const baseURL = "https://api.openweathermap.org/data/2.5/weather?zip=";
const apiKey = "&appid=";
const unit = "&units=imperial";
const button = document.getElementById("generate");
const today = new Date;
let zipCode = document.getElementById("zip").value;
let feeling = document.getElementById("feelings").value;

button.addEventListener("click", performAction);

function performAction() {
        getWeather(baseURL, zipCode, apiKey, unit)
        .then((data) => {
                console.log(data);
                postData("/", {
                        temperature: data.main.temp,
                        date: today.toDateString(),
                        response: feeling
                });
        })
        .then(updateUI())

}

const updateUI = async () => {
        const req = await fetch("/");

        try {
                const allData = await req.json();
                document.getElementById("temperature").innerHTML =
                        allData.temperature;
                document.getElementById("date").innerHTML =
                        allData.date;
                document.getElementById("insert-feeling") =
                        allData.response;
        } catch(error) {
                console.log("error", error);
        }
};

const getWeather = async (baseURL, zip, key, unit) => {
        const res = await fetch(baseURL+zip+key+unit);

        try {
                const data = await res.json();
                console.log(data);
                return data;
        } catch(error) {
                console.log("error", error);
        }
};
        

/* POST Route */
const postData = async (url = "", data = {}) => {
        console.log(data);
        const res = await fetch(url, {
                method: "POST",
                credentials: "same-origin",
                headers: {
                        "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
        });
        try {
                const newData = await res.json();
                console.log(newData);
        } catch(error) {
                console.log("error", error);
        }
};



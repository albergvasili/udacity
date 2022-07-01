/* SCRIPT */

const nav = document.querySelector("#nav-list");
const fragment = document.createDocumentFragment();

/* Create and add sections to the navigation menu */
for (let i = 1; i <= 4; i++) {
        let sectionNumber = document.querySelector(`#section${i}`)
        let sectionTitle = sectionNumber.firstElementChild;

        const listItem = document.createElement("li");
        listItem.classList.add("section-button");
        listItem.setAttribute("id", `nav-section${i}`);

        const anchorElement = document.createElement("a");
        anchorElement.setAttribute("href", `#section${i}`);
        anchorElement.innerText = sectionTitle.innerText;

        listItem.appendChild(anchorElement);

        fragment.appendChild(listItem);
};

nav.appendChild(fragment);


/* Scroll to section by cliking on navigation bar buttons */
for (let i = 1; i <= 4; i++) {
        let sectionButton = document.querySelector(`#nav-section${i}`);
        let sectionNumber = document.querySelector(`#section${i}`)
        let sectionCoordinates = sectionNumber.getBoundingClientRect();
        let topOfSection = sectionCoordinates.top;


        sectionButton.addEventListener("click", function () {
                scrollTo({
                        top: topOfSection - 50,
                        left: 0,
                        behavior: "smooth"
                })
        });               


                

};

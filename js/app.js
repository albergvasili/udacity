/* SCRIPT */
//TODO: Find a way to consolidate anchor and ul elements.


let sections = document.querySelectorAll("section");
const nav = document.querySelector("#nav-list");
const fragment = document.createDocumentFragment();

function createAnchorElement (index) {
        let sectionId = `#section${index}`;
        let sectionNumber = document.querySelector(sectionId);
        let sectionTitle = sectionNumber.firstElementChild;
        const anchorElement = document.createElement("a");

        anchorElement.setAttribute("href", sectionId);
        anchorElement.innerText = sectionTitle.innerText;

        return anchorElement
}

function createListItem (index) {
        const listItem = document.createElement("li");

        listItem.classList.add("section-button");
        listItem.setAttribute("id", `nav-section${index}`);

        return listItem;
}


for (let index = 1; index <= sections.length; index++) {
        
        //Create and add sections to the navigation menu
        let anchor = createAnchorElement(index);
        let list = createListItem(index);

        list.appendChild(anchor);
        fragment.appendChild(list);
}

nav.appendChild(fragment);


/* Scroll to a section by cliking on navigation bar buttons */
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
}


/* Change section class when it hits the top of the viewport */

window.addEventListener("scroll", function () {
        for (section of sections) {
                let sectionCoordinates = section.getBoundingClientRect();
                let topOfSection = sectionCoordinates.top;
                let bottomOfSection = sectionCoordinates.bottom;

                if (topOfSection >= -sectionCoordinates.height +200 && bottomOfSection <= window.innerHeight + 350) {
                        section.classList.add("active");
                } else {
                        section.classList.remove("active");
                }

        }
});


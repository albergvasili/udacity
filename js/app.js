/* SCRIPT */

const fragment = document.createDocumentFragment();
const nav = document.querySelector("#nav-list");
let sections = document.querySelectorAll("section");

function sectionId (index) {
        /* Get section ID. */
        let sectionId = `#section${index}`;
        return sectionId;
}

function sectionTitle (index) {
        /* Get section heading element title. */
        let sectionNumber = document.querySelector(sectionId(index));
        let sectionTitle = sectionNumber.firstElementChild;
        return sectionTitle;
}

function buttonId (index) {
        /* Get navigation bar button ID. */
        let navButtonId = `#nav-section${index}`;
        return navButtonId;
}

function createAnchorElement (index) {
        /* Create an anchor element based on section tags. */

        const anchorElement = document.createElement("a");

        anchorElement.setAttribute("href", sectionId(index));
        anchorElement.innerText = sectionTitle(index).innerText;

        return anchorElement
}

function createListItem (index) {
        /* Create li element for the navigation bar. */

        const listItem = document.createElement("li");

        listItem.classList.add("section-button");
        listItem.setAttribute("id", buttonId(index));

        return listItem;
}

function append (index) {
        /* Append list items and anchors to document fragment. */

        let anchor = createAnchorElement(index);
        let list = createListItem(index);

        list.appendChild(anchor);
        return fragment.appendChild(list);
}

        
for (let i = 1; i <= sections.length; i++) {
        
        append(i);
        nav.appendChild(fragment);
}

/* Scroll to a section by clicking on navigation bar buttons */

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


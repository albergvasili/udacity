/* SCRIPT */

const fragment = document.createDocumentFragment();
const nav = document.querySelector("#nav-list");
let sections = document.querySelectorAll("section");
let sectionInfo = [];

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
        let navButtonId = `nav-section${index}`;
        return navButtonId;
}

function createAnchorElement (index) {
        /* Create an anchor element based on section tags. */

        const anchorElement = document.createElement("a");

        anchorElement.setAttribute("href", sectionId(index));
        anchorElement.setAttribute("id", buttonId(index));
        anchorElement.classList.add("section-button");
        anchorElement.innerText = sectionTitle(index).innerText;

        return anchorElement
}

function createListItem (index) {
        /* Create li element for the navigation bar. */

        const listItem = document.createElement("li");
        listItem.classList.add("button-container");
        return listItem;
}

function append (index) {
        /* Append list items and anchors to document fragment. */

        let anchor = createAnchorElement(index);
        let list = createListItem(index);

        list.appendChild(anchor);
        return fragment.appendChild(list);
}

function sectionCoordinates () {
        /* Get section size and position relative to the viewport. */
        for (section of sections) {
                let sectionCoordinate = section.getBoundingClientRect();
                sectionInfo.push(sectionCoordinate);
        }
}

function scrollToSection (index) {
        /* Click button in navigation bar to scroll to desired section. */

        let sectionButton = document.querySelector("#" + buttonId(index));
        let topOfSection = sectionInfo[index - 1].top;


        sectionButton.addEventListener("click", function (event) {
                event.preventDefault();
                scrollTo({
                        top: topOfSection - 50,
                        left: 0,
                        behavior: "smooth"
                })
        });               

}

function activeSection () {
        /* Change section class when it hits the top of the viewport. */

        window.addEventListener("scroll", function () {
                for (section of sections) {
                        let sectionCoo = section.getBoundingClientRect();
                        let topOfSection = sectionCoo.top;
                        let bottomOfSection = sectionCoo.bottom;

                        if (topOfSection <= 100 && bottomOfSection >= 100) {
                                section.classList.add("active");
                        } else {
                                section.classList.remove("active");
                        }

                }
        });
}

for (let i = 1; i <= sections.length; i++) {
        
        append(i);
}

nav.appendChild(fragment);
sectionCoordinates();


for (let i = 1; i <= sections.length; i++) {
        scrollToSection(i);
}

activeSection();

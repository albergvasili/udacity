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
}

nav.appendChild(fragment);


/* 

scrollTo(coordinates);

*/


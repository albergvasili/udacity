/* SCRIPT */

const nav = document.querySelector("#nav-list");
const fragment = document.createDocumentFragment();

/* Create and add sections to the navigation menu */
for (let i = 1; i <= 4; i++) {
        const listItem = document.createElement("li");
        listItem.innerText = "Section " + i;
        listItem.classList.add("section-button");
        fragment.appendChild(listItem);
}

nav.appendChild(fragment);



let aboutTog = false;

let aboutClick = function () {
    let aboutBar = document.querySelector(".about");
    let aboutImg = document.querySelector(".about img");
    let aboutP = document.querySelector(".about p");

    if (aboutTog === false) {



        aboutBar.style.visibility = "visible";
        aboutBar.style.height = "200px";

        let len = 2;

        for (let i = 0; i < len; i++) {
            aboutImg.style.visibility = "visible";
            aboutP.style.visibility = "visible";
        }

        // aboutImg.style.visibility = "visible";
        // aboutP.style.visibility = "visible";


        aboutTog = true;

    }
    else if (aboutTog === true) {

        aboutBar.style.visibility = "hidden";
        aboutBar.style.height = "0px";


        let len = 2;

        for (let i = 0; i < len; i++) {
            aboutImg.style.visibility = "hidden";
            aboutP.style.visibility = "hidden";
        }

        // aboutImg.style.visibility = "hidden";
        // aboutP.style.visibility = "hidden";

        aboutTog = false;

    }
}

function scrollToSection(evt, sectionId) {
    // Scroll to the target section
    document.getElementById(sectionId).scrollIntoView({behavior: "smooth"});

    // Update the active class on the buttons
    var tablinks = document.getElementsByClassName("tablinks");
    for (var i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    evt.currentTarget.className += " active";
}
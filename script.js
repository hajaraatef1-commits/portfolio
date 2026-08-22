// ========================================
// JAVASCRIPT - PORTFOLIO HAJAR AATEF
// ========================================


// ================= MODE SOMBRE / CLAIR =================

const themeToggle = document.querySelector("#theme-toggle");

// Applique le thème sauvegardé au chargement
if (localStorage.getItem("theme") === "sombre") {

    document.body.classList.add("mode-sombre");

    if (themeToggle) {
        themeToggle.textContent = "☀️";
    }

}

if (themeToggle) {

    themeToggle.addEventListener("click", function() {

        document.body.classList.toggle("mode-sombre");

        const estSombre = document.body.classList.contains("mode-sombre");

        themeToggle.textContent = estSombre ? "☀️" : "🌙";

        localStorage.setItem("theme", estSombre ? "sombre" : "clair");

    });

}


// ================= ANIMATION AU DÉFILEMENT =================

const sectionsAnimees = document.querySelectorAll(".fade-section");

const observateur = new IntersectionObserver(function(entrees) {

    entrees.forEach(function(entree) {

        if (entree.isIntersecting) {

            entree.target.classList.add("visible");

        }

    });

}, {
    threshold: 0.15
});

sectionsAnimees.forEach(function(section) {

    observateur.observe(section);

});


// ================= BOUTON RETOUR EN HAUT =================

const boutonHaut = document.querySelector("#retour-haut");

if (boutonHaut) {

    window.addEventListener("scroll", function() {

        if (window.scrollY > 400) {

            boutonHaut.classList.add("visible");

        } else {

            boutonHaut.classList.remove("visible");

        }

    });

    boutonHaut.addEventListener("click", function() {

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

}


// ================= LOGIN =================

const EMAIL_AUTORISE = "hajaraatef1@gmail.com"; // <-- à personnaliser
const MOT_DE_PASSE = "aatef130904"; // <-- à personnaliser

const loginScreen = document.querySelector("#login-screen");
const loginForm = document.querySelector("#login-form");
const loginError = document.querySelector("#login-error");
const portfolioContent = document.querySelector("#portfolio-content");

// Si déjà connecté durant cette session, on saute l'écran de connexion
if (sessionStorage.getItem("connecte") === "oui") {

    loginScreen.style.display = "none";
    portfolioContent.style.display = "block";

}

if (loginForm) {

    loginForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const email = document.querySelector("#login-email").value.trim();
        const motDePasseSaisi = document.querySelector("#login-password").value;

        if (email === EMAIL_AUTORISE && motDePasseSaisi === MOT_DE_PASSE) {

            sessionStorage.setItem("connecte", "oui");

            loginScreen.style.display = "none";
            portfolioContent.style.display = "block";

            loginError.style.display = "none";

        } else {

            loginError.style.display = "block";

        }

    });

}


// ================= FORMULAIRE =================

const formulaire = document.querySelector("#contact-form");

if (formulaire) {

    formulaire.addEventListener("submit", function(event) {

        event.preventDefault();

        const nom = document.querySelector("#nom").value;
        const email = document.querySelector("#email").value;
        const message = document.querySelector("#message").value;

        if (nom === "" || email === "" || message === "") {

            alert("Veuillez remplir tous les champs.");

            return;
        }

        alert(
            "Merci " + nom +
            " ! Votre message a bien été envoyé."
        );

        formulaire.reset();

    });

}


// ================= ANIMATION DES PROJETS =================

const projets = document.querySelectorAll(".project-card");

projets.forEach(function(projet) {

    projet.addEventListener("mouseenter", function() {

        projet.style.transform = "translateY(-8px)";

    });

    projet.addEventListener("mouseleave", function() {

        projet.style.transform = "translateY(0)";

    });

});


// ================= COMPÉTENCES =================

const competences = document.querySelectorAll(".skill-card");

competences.forEach(function(skill) {

    skill.addEventListener("click", function() {

        skill.classList.toggle("selectionne");

    });

});


// ================= ANNÉE FOOTER =================

const annee = document.querySelector("#annee");

if (annee) {

    annee.textContent = new Date().getFullYear();

}


// ================= MESSAGE CONSOLE =================

console.log("Portfolio de Hajar Aatef chargé avec succès.");
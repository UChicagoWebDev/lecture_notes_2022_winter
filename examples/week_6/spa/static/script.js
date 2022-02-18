function makeBest(animal, pushHistory=true) {
  document.querySelectorAll(".animals .happy").forEach((n) => {n.setAttribute("style", "display: none")});
  document.querySelectorAll(".animals .sad").forEach((n) => {n.setAttribute("style", "display: block")});
  document.querySelectorAll(".animals ."+animal+" .sad").forEach((n) => {n.setAttribute("style", "display: none")});
  document.querySelectorAll(".animals ."+animal+" .happy").forEach((n) => {n.setAttribute("style", "display: block")});

  if (pushHistory) {
    history.pushState({"animal": animal}, animal+" is Best!", animal);
  }
}

function loadAnimal(pushHistory=true) {
  pathname = document.location.pathname;
  paths = pathname.split("/")
  animal = paths[1];
  if (animal.length > 0) {
    makeBest(animal, pushHistory);
  }
}

window.addEventListener("load", loadAnimal);
window.addEventListener("popstate", (newState) => {console.log(newState); loadAnimal(false)});

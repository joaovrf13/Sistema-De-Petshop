const sidebar = document.querySelector("#sidebar");
const backdrop = document.querySelector(".backdrop");
const modal = document.querySelector("#register-modal");
const search = document.querySelector("#global-search");

function openView(viewId) {
  document.querySelectorAll(".view").forEach((view) => {
    view.classList.toggle("active", view.id === viewId);
  });
  document.querySelectorAll(".nav-item[data-view]").forEach((item) => {
    item.classList.toggle("active", item.dataset.view === viewId);
  });
  sidebar.classList.remove("open");
  backdrop.classList.remove("show");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

document.querySelectorAll("[data-view], [data-view-link]").forEach((button) => {
  button.addEventListener("click", () => {
    openView(button.dataset.view || button.dataset.viewLink);
  });
});

document.querySelector(".menu-toggle").addEventListener("click", () => {
  sidebar.classList.add("open");
  backdrop.classList.add("show");
});

document.querySelector(".close-menu").addEventListener("click", () => {
  sidebar.classList.remove("open");
  backdrop.classList.remove("show");
});

backdrop.addEventListener("click", () => {
  sidebar.classList.remove("open");
  backdrop.classList.remove("show");
});

document.querySelectorAll(".open-modal").forEach((button) => {
  button.addEventListener("click", () => modal.showModal());
});

document.querySelectorAll(".modal-close").forEach((button) => {
  button.addEventListener("click", () => modal.close());
});

modal.addEventListener("click", (event) => {
  if (event.target === modal) modal.close();
});

search.addEventListener("input", () => {
  const term = search.value.trim().toLocaleLowerCase("pt-BR");
  if (term) openView("clientes");

  const rows = [...document.querySelectorAll("#clientes .searchable")];
  let visible = 0;
  rows.forEach((row) => {
    const match = row.textContent.toLocaleLowerCase("pt-BR").includes(term);
    row.hidden = !match;
    if (match) visible += 1;
  });

  const empty = document.querySelector(".search-empty");
  if (empty) empty.hidden = !term || visible > 0;
});

document.querySelectorAll(".flash button").forEach((button) => {
  button.addEventListener("click", () => button.parentElement.remove());
});
window.setTimeout(() => document.querySelectorAll(".flash").forEach((item) => item.remove()), 4500);

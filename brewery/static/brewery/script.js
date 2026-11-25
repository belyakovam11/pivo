const accountModal = document.querySelector("#account-modal");
const eventModal = document.querySelector("#event-modal");
const projectModal = document.querySelector("#project-modal");
const accountForm = document.querySelector("#account-form");
const accountTypes = document.querySelector(".account-types");
const accountFormTitle = document.querySelector("#account-form-title");
const wholesaleField = document.querySelector(".wholesale-only");
const buyerTypeInput = accountForm.querySelector('[name="buyer_type"]');

function openModal(modal) {
  if (typeof modal.showModal === "function") modal.showModal();
}

document.querySelectorAll("[data-open-account]").forEach((button) => {
  button.addEventListener("click", () => {
    accountTypes.hidden = false;
    accountForm.hidden = true;
    openModal(accountModal);
  });
});

document.querySelectorAll("[data-close-modal]").forEach((button) => {
  button.addEventListener("click", () => button.closest("dialog").close());
});

document.querySelectorAll("dialog").forEach((dialog) => {
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });
});

document.querySelectorAll("[data-account-type]").forEach((button) => {
  button.addEventListener("click", () => {
    const isWholesale = button.dataset.accountType === "wholesale";
    accountTypes.hidden = true;
    accountForm.hidden = false;
    wholesaleField.hidden = !isWholesale;
    wholesaleField.querySelector("input").required = isWholesale;
    buyerTypeInput.value = button.dataset.accountType;
    accountFormTitle.textContent = isWholesale ? "Регистрация оптового покупателя" : "Регистрация частного покупателя";
  });
});

document.querySelector("[data-back-account]").addEventListener("click", () => {
  accountTypes.hidden = false;
  accountForm.hidden = true;
});

document.querySelectorAll("[data-event]").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelector("#event-modal-title").textContent = button.dataset.event;
    document.querySelector("#event-title-input").value = button.dataset.event;
    openModal(eventModal);
  });
});

document.querySelector("[data-open-project]").addEventListener("click", () => openModal(projectModal));

function showToast(message) {
  const toast = document.querySelector("#toast");
  toast.textContent = message;
  toast.classList.add("visible");
  window.setTimeout(() => toast.classList.remove("visible"), 3200);
}

const serverMessage = document.querySelector(".server-messages span");
if (serverMessage) showToast(serverMessage.textContent);

const menuButton = document.querySelector(".menu-button");
const nav = document.querySelector(".nav");
menuButton.addEventListener("click", () => {
  const isOpen = nav.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(isOpen));
});
nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => {
  nav.classList.remove("open");
  menuButton.setAttribute("aria-expanded", "false");
}));

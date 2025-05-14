const messagesContainer = document.querySelector('.messages');

function scrollToBottom() {
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

scrollToBottom();

function copyToClipboard(code) {
  navigator.clipboard.writeText(code).then(() => {
    alert("Code copied!");
  });
}

function handleFileSelection(event) {
  const fileInput = event.target;
  const messageBox = document.getElementById('messageBox');

  if (fileInput.files.length > 0) {
    messageBox.value = fileInput.files[0].name + " attached. ";
  } else {
    messageBox.value = "";
  }
}

function handleSend(event) {
  const fileInput = document.getElementById('fileInput');
  const messageBox = document.getElementById('messageBox');
  const messagesContainer = document.getElementById('messages');

  if (fileInput.files.length === 0 && messageBox.value.trim() === "") {
    alert("Please enter a message or select a file to send.");
    event.preventDefault();
    return;
  }

  setTimeout(() => {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }, 100);

}
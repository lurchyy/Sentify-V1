function sendCommentsToFlask(comments) {
  fetch('http://localhost:5000/process_comments', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ comments })
  })
    .then(response => response.json())
    .then(data => {
      console.log(data.message);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  // console message dekne ke liye extension right click kar aur inspect me jaa, page refresh kar for logs
  sendCommentsToFlask(message)
});
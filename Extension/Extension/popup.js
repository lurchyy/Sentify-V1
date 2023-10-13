
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  // console.log(typeof message);
  // console.log(JSON.stringify(message));
  sendCommentsToFlask(message)
});
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

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  // console message dekne ke liye extension right click kar aur inspect me jaa, page refresh kar for logs
  console.log('Received message from content.js:', message);
});

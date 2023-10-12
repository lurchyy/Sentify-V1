

function getRedditAnswers() {
    const title = document.querySelector('h1').textContent;
    const comments = document.querySelectorAll('div[data-testid="comment"]');
    const len = comments.length;
    const lent = Math.min(len, 25);

    chrome.runtime.sendMessage({ title });

    for (let i = 0; i < lent; i++) {
        const comment = comments[i].textContent;
        chrome.runtime.sendMessage({ comment });
    }
}


function getQuoraAnswers() {
    const question_box = document.querySelector('div[class="q-text qu-dynamicFontSize--xlarge qu-fontWeight--bold qu-color--gray_dark_dim qu-passColorToLinks qu-lineHeight--regular qu-wordBreak--break-word"]');
    const question = question_box.textContent;
    chrome.runtime.sendMessage({ question });

    const answers = document.querySelectorAll('div[class="q-box qu-cursor--pointer QTextTruncated___StyledBox-sc-1pev100-0 gCXnis"]');
    const len = answers.length;
    const lent = Math.min(len, 5);

    chrome.runtime.sendMessage({ len });

    for (let i = 0; i < lent; i++) {
        const answer = answers[i].textContent;
        chrome.runtime.sendMessage({ answer });
    }
}








if (window.location.href.includes('reddit.com')) {
    getRedditAnswers();
}
else if (window.location.href.includes('quora.com')) {
    getQuoraAnswers();
}


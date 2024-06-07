function coin_click() {
    //get mouse coordinates
    const mouseX = event.clientX;
    const mouseY = event.clientY;
  
    //set div styles and text
    const messageDiv = document.createElement('div');
    messageDiv.style.position = 'absolute';
    messageDiv.style.left = mouseX + 'px';
    messageDiv.style.top = mouseY + 'px';
    messageDiv.style.color = 'white';
    messageDiv.style.fontSize = '32px';
    messageDiv.style.opacity = 1;
    messageDiv.textContent = '+1';
  
    //apply div to html
    document.body.appendChild(messageDiv);
  
    //create a animation for div
    const animation = messageDiv.animate(
        [{ top: mouseY - 50 + 'px', opacity: 1 },{ top: mouseY - 110 + 'px', opacity: 0 }],
        {duration: 1000}
    );

    //remove div from html when animation ended
    animation.onfinish = () => {
      document.body.removeChild(messageDiv);
    };
}
  
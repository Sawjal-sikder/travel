const waterEffect = document.getElementById("water-effect");

let offset = 0;
function animateWater() {
    offset += 0.5; // Control the speed of the wave
    waterEffect.style.backgroundPositionY = `${offset}px`; // Moves the gradient to create the effect
    requestAnimationFrame(animateWater); // Continuously animate the wave effect
  }

 animateWater();

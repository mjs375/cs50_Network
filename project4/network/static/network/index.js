/*

// JAVASCRIPT

// Wait til page is fully loaded, then check-if...:
document.addEventListener('DOMContentLoaded', function() {
  // Use buttons to toggle views(pages):
document.querySelector('#squeak_button').addEventListener('click', () => compose_squeak());

});



// 1. Prepares Compose Squeak form:
function compose_squeak() {
  // Reveal the 'compose_squeak' <div>:
  document.querySelector('#compose-view').style.display = 'block';
  // Clear out composition fields:
  document.querySelector("#compose-message").value = '';
} // * * * * * * * * * * * * * * * * * * * * * * * *

// 2. Processes data from a submitted form:
function submit_squeak_form() {
  // Get post contents from form <input>
  const msg = document.querySelector('#compose-message').value;
  // Call post function, providing values from form
  post_squeak(msg);
} // * * * * * * * * * * * * * * * * * * * * * * * *

// 3. Posts the Squeak:
function post_squeak(msg) {
  fetch

} // * * * * * * * * * * * * * * * * * * * * * * * *







#
*/

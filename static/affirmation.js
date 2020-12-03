"use strict";

$.get('/', (response) => {
  $('#affirmation').text(response);
});
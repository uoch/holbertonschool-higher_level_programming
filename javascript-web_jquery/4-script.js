#!/usr/bin/node
$(document).ready(() => {
    $('DIV#toggle_header').on('click', () => {
      $('header').toggleClass('red green');
    });
  });

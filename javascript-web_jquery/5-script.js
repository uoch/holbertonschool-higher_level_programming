#!/usr/bin/node
$(document).ready(() => {
    $('DIV#add_item').on('click', () => {
      $('ul.my_list').append('<li>Item</li>');
    });
  });

//@format
const fs = require('fs');

// 2/1/19
// this code is a mess but it works. It adds p or c widgets to white/grey/black
// lists and cleans and maintains those lists in the process.
// One thing that might be confusing is that the global_status column shown on
// the web app always (whether in development or production) comes from ulanmedia.brianhaller.net.
// In development, adding to list only impacts the development white/grey/black
// lists. However the global_status column still comes from
// ulanmedia.brianhaller.net when in development.

function addToList(widgetID, listType) {
  const currentListStatus = getCurrentListStatus(widgetID);
  let message = '';
  if (widgetID.trim() === '') {
    message = 'widget not added to list - invalid id';
    return message;
  }
  for (let key in currentListStatus) {
    if (key === listType && currentListStatus[key] === true) {
      if (message === '') {
        message = `widget already in ${listType} list`;
      } else {
        message += ` and already in ${listType} list`;
      }
    } else if (key === listType && currentListStatus[key] === false) {
      writeToList(widgetID, key);
      if (message === '') {
        message = `widget added to ${listType} list`;
      } else {
        message += ` and added to ${listType} list`;
      }
    } else if (currentListStatus[key] === true) {
      eraseFromList(widgetID, key);
      if (message === '') {
        message = `widget erased from ${key} list`;
      } else {
        message += ` and erased from ${key} list`;
      }
    }
  }
  return message;
}

function writeToList(widgetID, listType) {
  // This function is kind of convoluted but it just adds a widget id to a
  // list.
  // It handles the cases of extra white space or extra lines.
  let widgets = fs
    .readFileSync(`../../widget_lists/${listType}list.txt`, 'utf8')
    .trim()
    .split('\n');
  const widgetsWithoutBlankLines = [];
  for (let i = 0; i < widgets.length; i++) {
    if (widgets[i] !== '') {
      widgetsWithoutBlankLines.push(widgets[i].trim());
    }
  }
  const widgetsWithoughBlankLinesAndWithNewWidgetID = widgetsWithoutBlankLines.concat(
    widgetID,
  );

  fs.writeFileSync(
    `../../widget_lists/${listType}list.txt`,
    widgetsWithoughBlankLinesAndWithNewWidgetID.join('\n'),
  );
}

function eraseFromList(widgetID, listType) {
  let widgets = fs
    .readFileSync(`../../widget_lists/${listType}list.txt`, 'utf8')
    .trim()
    .split('\n');
  const widgetsWithoutBlankLines = [];
  for (let i = 0; i < widgets.length; i++) {
    if (widgets[i] !== '') {
      widgetsWithoutBlankLines.push(widgets[i].trim());
    }
  }
  const widgetsWithoutBlankLinesAndWithWidgetIDRemoved = [];
  for (let i = 0; i < widgets.length; i++) {
    if (widgetsWithoutBlankLines[i] !== widgetID) {
      widgetsWithoutBlankLinesAndWithWidgetIDRemoved.push(
        widgetsWithoutBlankLines[i],
      );
    }
  }

  fs.writeFileSync(
    `../../widget_lists/${listType}list.txt`,
    widgetsWithoutBlankLinesAndWithWidgetIDRemoved.join('\n'),
  );
}

function getCurrentListStatus(widgetID) {
  const currentListStatus = {
    white: false,
    grey: false,
    black: false,
  };
  if (isInWhiteList(widgetID)) {
    currentListStatus.white = true;
  }
  if (isInGreyList(widgetID)) {
    currentListStatus.grey = true;
  }
  if (isInBlackList(widgetID)) {
    currentListStatus.black = true;
  }
  return currentListStatus;
}

function isInWhiteList(widgetID) {
  const widgets = fs
    .readFileSync(`../../widget_lists/whitelist.txt`, 'utf8')
    .trim()
    .split('\n');
  for (let id of widgets) {
    if (id === widgetID) {
      return true;
    }
  }
  return false;
}

function isInGreyList(widgetID) {
  const widgets = fs
    .readFileSync(`../../widget_lists/greylist.txt`, 'utf8')
    .trim()
    .split('\n');
  for (let id of widgets) {
    if (id === widgetID) {
      return true;
    }
  }
  return false;
}

function isInBlackList(widgetID) {
  const widgets = fs
    .readFileSync(`../../widget_lists/blacklist.txt`, 'utf8')
    .trim()
    .split('\n');
  for (let id of widgets) {
    if (id === widgetID) {
      return true;
    }
  }
  return false;
}

module.exports = addToList;

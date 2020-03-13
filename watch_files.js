module.exports = function filter(file) {
  if (file.endsWith('tailwind.config.js')) {
    return true;
  }
  return false;
};

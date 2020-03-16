const path = require('path');
const purgecss = require('@fullhuman/postcss-purgecss');
const tailwindcss = require('tailwindcss');
const postcssNested = require('postcss-nested');
const production = process.env.FRAPPE_ENV === 'production';

module.exports = {
  plugins: [
    tailwindcss(path.resolve(__dirname, './tailwind.config.js')),
    postcssNested,
    production
      ? purgecss({
          content: ['./frappebooks_com/**/*.html'],
          defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
        })
      : null,
    production ? require('cssnano')({ preset: 'default' }) : null
  ].filter(Boolean)
};

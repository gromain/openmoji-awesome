# Openmoji-awesome 💡

**Like Font-Awesome and Twemoji-amazing, but for Openmoji Emojis!** 🌟

It's CSS classes for all your Emoji needs, now with all the Creative Commons goodness!

_Forked from [twemoji-amazing](https://github.com/SebastianAigner/twemoji-amazing)!_

![openmoji-banner](openmoji-banner.png)

### Usage

#### Basic Usage

Add the main files `openmoji-color-awesome.css` and `openmoji-black-awesome.css` to your project and then simply use the following in your HTML source:

`<i class="oma oma-face-with-monocle"></i>`

#### Size Options

Like in Font-Awesome, emoji sizes can be changed via `oma-lg`, `oma-bg`, `oma-2x`, `oma-3x`, `oma-4x`, and `oma-5x`.

#### Finding Emojis

- Openmoji-awesome uses [Openmoji json data](https://github.com/hfg-gmuend/openmoji/blob/master/data/openmoji.json) as its source of codepoints and descriptions.
- To find an emoji of your liking, check out the [Openmoji emoji list](https://openmoji.org/library/). Replace spaces with hyphens to get the class name! (e.g. "man in suit levitating" becomes `oma-man-in-suit-levitating` or `oma-black-man-in-suit-levitating` 🕴)

To use on your website, it is advised to download the svg files here: https://github.com/hfg-gmuend/openmoji/releases/tag/13.1.0 .
By default, the script will generate a css file that will uses the emoji distributed from jsdeliver CDN.


#### Running the generator

`./gradlew run` will generate a fresh version of both the `openmoji-color-awesome.css` and the `openmoji-black-awesome.css` file in the root directory of the project.

The script source can be found in `src/main/kotlin/Main.kt` if you want to customize the image path (Change `openmojiColorUrl` and `openmojiBlackUrl` to the URL you want to use as a source).

You can integrate those in your project to use either color or black and white (or both!) emojis from Openmoji.

### Licenses & Other

License: [MIT](https://mit-license.org/).

Uses CSS snippets from [twemoji-awesome](https://github.com/ellekasai/twemoji-awesome), licensed under [MIT](http://ellekasai.mit-license.org/).

Uses base code from [twemoji-amazing](https://github.com/SebastianAigner/twemoji-amazing), licensed under [MIT](https://mit-license.org/).

As per the Openmoji repository, the graphics are licensed under the CC-BY 4.0 which has a pretty good guide on [best practices for attribution](https://wiki.creativecommons.org/Best_practices_for_attribution).

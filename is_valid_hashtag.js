/*
 * is_valid_hashtag
 *
 * 2018 Caleb Ely
 * <https://github.com/le717/is-valid-hashtag>
 *
 * The Unlicense
 * <http://unlicense.org/>
 */


/**
 * Check if a hashtag is valid.
 *
 * @param {String} hashtag Check if a hashtag is valid.
 * @returns {Boolean} True for valid hashtag, False otherwise.
 */
export default function is_valid_hashtag(hashtag) {
    "use strict";
    return /#(?:[a-z]|(?:\d|_)[a-z])\w+/i.test(hashtag);
}

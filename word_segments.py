
def get_words(input_str, words_dict, prefix_count):
	valid_words = []
	if words_dict.get(input_str):
		valid_words.append(words_dict[input_str])
	else:
	    str_len = len(input_str)
	    end_idx = prefix_count
	    maybe_word = input_str[0:end_idx]
	    while not words_dict.get(maybe_word) and end_idx < str_len:
	        end_idx += 1
	        maybe_word = input_str[0:end_idx]
	        
	    if words_dict.get(maybe_word):
	        valid_words.append(maybe_word)
	        remaining_str_words = get_words(input_str[end_idx:], words_dict, 0)
	        if remaining_str_words:
	            valid_words = valid_words + remaining_str_words
	        else:
	            valid_words = get_words(input_str, words_dict, prefix_count+1)
	return valid_words

        
print(get_words("applepie", {"a":"a", "apple":"apple", "pie":"pie"}, 0))
print(get_words("aaaaapplepie", {"a":"a", "app":"app", "apple":"apple", "pie":"pie"}, 0))
print(get_words("bestbuybest", {"best":"best", "buy":"buy"}, 0))
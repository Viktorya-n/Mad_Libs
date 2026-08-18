# Mad Libs Station 🎭

A simple command-line **Mad Libs game written in Python**. The player chooses one of three story templates and fills in blanks with different types of words. The program validates the user's input and then generates a funny story using the supplied words.

## Features

* 🎮 Three different Mad Libs story templates
* 🔢 Input validation for numbers
* ⏰ Validation for measures of time
* 🔤 Validation for words containing letters only
* 🏃 Validation for words ending in `-ing`
* 🚀 Validation for adverbs ending in `-ly`
* 🎲 Automatically selects a random template if an invalid template number is entered
* 🛑 Handles `Ctrl+C` and end-of-file input gracefully
* 📖 Prints the completed story after all inputs are provided

## Requirements

* Python 3.x
* No external libraries are required

The program only uses Python's built-in `random` module.

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the directory containing `mad_libs.py`.
3. Run:

```bash
python mad_libs.py
```

Depending on your system, you may need to use:

```bash
python3 mad_libs.py
```

## How to Play

When the program starts, you will see:

```text
___Mad Libs Station___

Pick a template (1, 2, or 3):
```

Enter:

* `1` for the **Hospital** story
* `2` for the **Camping** story
* `3` for the **Enchanted Castle** story

You will then be asked to provide different types of words.

### Template 1 — Hospital

The first story asks for words such as:

* Number
* Measure of time
* Mode of transportation
* Adjectives
* Nouns
* Color
* Parts of the body
* Verbs
* A silly word

### Template 2 — Camping

The second story asks for:

* Person's name
* Nouns
* Feelings
* Verbs
* Animals
* Colors
* An `-ing` word
* An `-ly` adverb
* Numbers
* Measures of time
* A silly word

### Template 3 — Enchanted Castle

The third story asks for:

* Person's name
* Adjectives
* Colors
* Animals
* Places
* Magical creatures
* Rooms
* Nouns
* Plural nouns
* Numbers
* Measures of time
* An `-ing` word

## Input Validation

The program uses the `get_input()` function to validate user responses.

### Number

Only digits are accepted.

Example:

```text
Number: 25
```

### Measure of Time

The following values are accepted:

* second / seconds
* minute / minutes
* hour / hours
* day / days
* week / weeks
* month / months
* year / years

### `-ing` Words

The input must end with `ing` and contain letters/spaces only.

Example:

```text
Verb (ending in ing): hiking
```

### `-ly` Words

The input must end with `ly`.

Example:

```text
Adverb (ending in ly): quickly
```

### Regular Words

Regular word inputs must contain letters and may contain spaces.

If the user leaves an input blank, the program asks them to try again.

## Project Structure

```text
.
├── mad_libs.py
└── README.md
```

## Main Functions

### `get_input(prompt, validation_type="word")`

Handles user input and validates it according to the requested type.

Supported validation types include:

* `number`
* `ing`
* `ly`
* `word`
* `measure of time`
* `any`

### `play_mad_libs()`

Runs the main game. It:

1. Displays the game title.
2. Asks the player to select a template.
3. Collects the required words.
4. Builds the selected story.
5. Displays the completed story.

### `ExitGame`

A custom exception used to exit the game when the user interrupts input with `Ctrl+C` or when an EOF occurs.

## Error Handling

If an invalid template is entered, the program does not stop. Instead, it randomly selects one of the three templates.

For invalid word input, the program displays an error message and asks the user to enter the value again.

The program also catches:

```python
KeyboardInterrupt
EOFError
```

and exits with a short goodbye message.

## Example

A completed story might look something like:

```text
___YOUR STORY___

It was about 3 days ago when I arrived at the hospital in a train.
The hospital is a strange place, there are a lot of noisy doctors here.
...
```

The exact story will change depending on the player's answers.

## Technologies Used

* **Python 3**
* Python's built-in `random` module

## Future Improvements

Possible improvements include:

* Add more story templates
* Add a replay option without restarting the program
* Allow players to create their own templates
* Improve validation for specific parts of speech
* Add colored terminal output
* Save completed stories to a text file
* Keep track of previously played stories
* Add a graphical user interface (GUI)

## License

This project is provided for educational and personal use.

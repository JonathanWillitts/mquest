"""mquest:  Python Mathematics Question Generator

Code to generate multiplication, mixed multiplication and division questions.
"""
import argparse
import calendar
import pathlib
import random
from random import shuffle
from typing import List


def generate_multiplications(multiplier: int, shuffle_order: bool = False
                             ) -> List[str]:
    """Returns a list of multiplication questions for the given multiplier."""
    # Define multiplicands (i.e. numbers 1-12)
    multiplicands = list(range(1, 13))

    if shuffle_order:
        # Randomise order
        shuffle(multiplicands)

    # Build multiplication questions list, and return
    questions = []
    for multiplicand in multiplicands:
        questions.append(f"{multiplicand: >2} x {multiplier} = ")

    return questions


def generate_mixed_multiplications(multipliers: [int]) -> List[str]:
    """Returns a list of mixed multiplication questions for the given
    multipliers (plural).
    """
    # Define multiplicands (i.e. numbers 1-12)
    multiplicands = list(range(1, 13))

    # Randomise order of multiplicands
    shuffle(multiplicands)

    # Build multiplication questions list, and return
    questions = []
    for multiplicand in multiplicands:
        questions.append(f"{multiplicand: >2} x {random.choice(multipliers)} = ")

    return questions


def generate_divisions(divisor: int) -> List[str]:
    """Returns a list of division questions for the given divisor."""
    # Define dividends (i.e. numbers 1-12), and randomise order
    dividends = [index * divisor for index in range(1, 13)]
    shuffle(dividends)

    # Build division questions list, and return
    questions = []
    division_sign_unicode = '\u00F7'
    for dividend in dividends:
        questions.append(f"{dividend: >3} {division_sign_unicode} {divisor} = ")

    return questions


def get_days_of_week(first_day: int = calendar.MONDAY) -> List[str]:
    """Returns a list of ordered days, starting with the specified day."""
    calendar.setfirstweekday(first_day)
    return list(calendar.day_name[calendar.firstweekday():]
                + calendar.day_name[0:calendar.firstweekday()])


def format_questions(heading: str, questions: List[str]) -> str:
    """Formats question list with given heading."""
    new_line = '\n'
    return(
        f"{heading}:\n"
        f"{(len(heading) + 1) * '-'}\n"
        f"{new_line.join(questions)}\n\n"
    )


def main() -> None:
    """Offers CLI when when py-mquest run as a standalone script."""
    parser = argparse.ArgumentParser(
        description='Python Mathematics Question Generator.')
    parser.add_argument(
        '-m', '--mode',
        choices=('m', 'mm', 'd'),
        help="Mode, either: 'm' (multiplication), 'mm' (mixed multiplication) "
             " or 'd' (division).",
        required=True,
    )
    parser.add_argument(
        '-o', '--operands',
        type=int,
        nargs='+',
        help="The operand(s) to apply to the specified mode "
             "(e.g. used to multiply or divide by). "
             "For mixed multiplications specify multiple operands.",
        required=True,
    )
    parser.add_argument(
        '-s', '--shuffle',
        action='store_true',
        help="Shuffle order of generated questions "
             "(applies to multiplications mode only).",
        default=False,
    )
    parser.add_argument(
        '-d', '--start-day',
        choices=(range(0, 7)),
        type=int,
        help="Start day, (0 for Monday, 1 for Tuesday, ..., 6 for Sunday).",
    )
    parser.add_argument(
        '-f', '--file',
        type=pathlib.Path,
        help="If specified write to output file instead of printing to stdout.",
    )
    args = parser.parse_args()

    # Define heading(s) for each question set
    if args.start_day is not None:
        headings = get_days_of_week(first_day=args.start_day)
    else:
        headings = ['Questions']

    # Generate questions (based on specified mode)
    questions = []
    count = 0
    for heading in headings:
        count += 1
        if args.mode == 'm':
            # Generate multiplication questions
            questions.append(format_questions(
                heading=heading,
                questions=generate_multiplications(multiplier=args.operands[0],
                                                   shuffle_order=args.shuffle),
            ))

        elif args.mode == 'mm':
            # Generate mixed multiplication questions
            questions.append(format_questions(
                heading=heading,
                questions=generate_mixed_multiplications(multipliers=args.operands),
            ))

        elif args.mode == 'd':
            # Generate division questions
            questions.append(format_questions(
                heading=heading,
                questions=generate_divisions(divisor=args.operands[0])
            ))

    # If output file specified
    if args.file is not None:
        # Write to output file
        with args.file.open('w') as out_file:
            out_file.writelines(questions)
    else:
        # Print to stdout
        print("".join(questions))


if __name__ == "__main__":
    main()

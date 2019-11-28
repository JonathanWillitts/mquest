"""Documented mquest examples."""
import calendar

from mquest import mquest


def main() -> None:
    """Examples"""
    # Generate a raw list of ordered 11 times table questions
    times_11_questions = mquest.generate_multiplications(multiplier=11)

    # Format and print them, with a heading
    print(mquest.format_questions(heading="11 x table questions",
                                  questions=times_11_questions))

    # Generate a single set of 8 times tables questions, shuffle the order,
    # format, and print
    print(mquest.format_questions(
        heading="8 x table questions (shuffled)",
        questions=mquest.generate_multiplications(multiplier=8,
                                                  shuffle_order=True),
    ))

    # Generate a single set of division by 4 questions in shuffled order,
    # format, and print
    print(mquest.format_questions(
        heading="รท (divide by) 4 questions",
        questions=mquest.generate_divisions(divisor=4)
    ))

    # Define list of study days (i.e. days to generate questions for),
    # for each day of the week, starting on Friday
    study_days = mquest.get_days_of_week(first_day=calendar.FRIDAY)

    # Generate daily 3 times tables questions, in order, format, and print
    # (for each day of the week)
    for day in study_days:
        print(mquest.format_questions(
            heading=day,
            questions=mquest.generate_multiplications(multiplier=3),
        ))

    # Generate daily, mixed, shuffled questions for 2, 3, 4, 5, 6, 8 & 10
    # times tables, format, and print (for each day of the week)
    for day in study_days:
        print(mquest.format_questions(
            heading=day,
            questions=mquest.generate_mixed_multiplications(
                multipliers=list([2, 3, 4, 5, 6, 8, 10])),
        ))


if __name__ == "__main__":
    main()

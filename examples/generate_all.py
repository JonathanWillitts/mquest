"""Generates multiplication (ordered and unordered) and division question files
for 1 to 12 times tables.
"""
import calendar
import pathlib

from mquest import mquest


def main() -> None:
    """Generates question files."""
    # Define start day (of each week)
    study_days = mquest.get_days_of_week(first_day=calendar.SUNDAY)

    # Define path to write files to, and ensure it exists
    output_path = pathlib.Path('output')
    output_path.mkdir(parents=True, exist_ok=True)

    # Define operands (here we assume we want to generate 1-12 times tables)
    operands = list(range(1, 13))

    for operand in operands:
        # Generate ordered times tables questions for this operand
        file = output_path / f'{operand}_times_table_ordered.txt'
        with file.open(mode='w', encoding='utf-8') as out_file:
            for day in study_days:
                out_file.writelines(
                    mquest.format_questions(
                        heading=day,
                        questions=mquest.generate_multiplications(
                            multiplier=operand,
                            shuffle_order=False,
                        ),
                    )
                )

        # Generate unordered times tables questions for this operand
        file = output_path / f'{operand}_times_table_unordered.txt'
        with file.open(mode='w', encoding='utf-8') as out_file:
            for day in study_days:
                out_file.writelines(
                    mquest.format_questions(
                        heading=day,
                        questions=mquest.generate_multiplications(
                            multiplier=operand,
                            shuffle_order=True,
                        ),
                    )
                )

        # Generate division questions for this operand
        file = output_path / f'divide_by_{operand}.txt'
        with file.open(mode='w', encoding='utf-8') as out_file:
            for day in study_days:
                out_file.writelines(
                    mquest.format_questions(
                        heading=day,
                        questions=mquest.generate_divisions(
                            divisor=operand,
                        ),
                    )
                )


if __name__ == "__main__":
    main()

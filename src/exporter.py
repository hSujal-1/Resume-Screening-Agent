import csv
import json


def export_to_csv(results, output_path):
    """
    Export ranked resumes to a CSV file.
    """

    with open(output_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Rank", "Filename", "Similarity Score"])

        for index, result in enumerate(results, start=1):

            writer.writerow([
                index,
                result["filename"],
                round(result["score"], 4)
            ])

    print(f"\nCSV exported successfully: {output_path}")


def export_to_json(results, output_path):
    """
    Export ranked resumes to a JSON file.
    """

    with open(output_path, "w", encoding="utf-8") as file:

        json.dump(
            results,
            file,
            indent=4
        )

    print(f"JSON exported successfully: {output_path}")
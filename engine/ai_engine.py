def generate_ai_summary(report):

    summary = []

    for item in report:

        if item["state"] == "strong":

            summary.append(
                f"{item['planet']} gives strong positive effects."
            )

        elif item["state"] == "combust":

            summary.append(
                f"{item['planet']} may create internal stress."
            )

    return summary

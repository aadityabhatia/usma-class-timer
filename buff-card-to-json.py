import marimo

__generated_with = "unknown"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from icalendar import Calendar
    from datetime import datetime
    from io import BytesIO
    return Calendar, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Upload Buff Card""")
    return


@app.cell(hide_code=True)
def _(mo):
    ics = mo.ui.file(filetypes=['.ics'], kind='area')
    ics
    return (ics,)


@app.cell(hide_code=True)
def _(Calendar, ics, mo):
    mo.stop(ics.contents() == None, mo.md("**_Please upload the buff card ICAL from AMS to proceed._**"))

    cal = Calendar.from_ical(ics.contents())

    DAYS = {}

    # Iterate through events
    for component in cal.walk():
        if component.name == "VEVENT":
            # Extract event summary/title
            summary = str(component.get('summary', ''))

            # Check if the summary starts with '1-' or '2-'
            if summary.startswith('1-') or summary.startswith('2-'):
                # Get event date
                start_time = component.get('dtstart').dt

                # Format the date as YYYY-MM-DD
                date_str = start_time.strftime("%Y-%m-%d")

                # check if it is a 1- or 2- event
                DAYS[date_str] = int(summary.split('-')[0])

    DAYS
    return


if __name__ == "__main__":
    app.run()

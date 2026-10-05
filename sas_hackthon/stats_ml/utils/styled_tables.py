"""
Styled HTML table display utilities for Jupyter notebooks.

Usage (from any notebook inside sas_hackthon/stats_ml/):
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.dirname("__file__")))
    from utils import display_styled_table, display_table_with_stats, TABLE_COLORS

Or with a direct import:
    from utils.styled_tables import display_styled_table
"""

from IPython.display import HTML, display


# ---------------------------------------------------------------------------
# Predefined color schemes for easy use
# ---------------------------------------------------------------------------
TABLE_COLORS = {
    "green": "#4CAF50",
    "blue": "#2196F3",
    "orange": "#FF9800",
    "red": "#F44336",
    "purple": "#9C27B0",
    "teal": "#009688",
    "indigo": "#3F51B5",
    "cyan": "#00BCD4",
    "lime": "#8BC34A",
    "pink": "#E91E63",
}


# ---------------------------------------------------------------------------
# Core display functions
# ---------------------------------------------------------------------------
def display_styled_table(
    df,
    title=None,
    header_color="#4CAF50",
    font_size="11px",
    width="100%",
    alternate_rows=True,
    hover_effect=True,
):
    """
    Display a pandas DataFrame as a styled HTML table.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to display.
    title : str, optional
        Title to display above the table.
    header_color : str, default "#4CAF50"
        Background color for the header row (hex or CSS color name).
        Examples: "#4CAF50" (green), "#2196F3" (blue), "#FF9800" (orange).
    font_size : str, default "11px"
        Font size for the table content.
    width : str, default "100%"
        CSS width for the table.
    alternate_rows : bool, default True
        Whether to alternate row background colors.
    hover_effect : bool, default True
        Whether to highlight the row under the cursor.

    Examples
    --------
    >>> display_styled_table(df)
    >>> display_styled_table(df, title="Sales Data", header_color="#2196F3")
    >>> display_styled_table(df, hover_effect=False)
    """
    if title:
        print("\n" + "=" * 120)
        print(title)
        print("=" * 120)

    html_table = df.to_html(index=False, border=1, justify="center")

    css_styles = f"""
    <style>
        table {{
            border-collapse: collapse;
            width: {width};
            font-size: {font_size};
        }}
        th {{
            background-color: {header_color};
            color: white;
            padding: 8px;
            text-align: center;
            font-weight: bold;
        }}
        td {{
            padding: 6px;
            text-align: center;
            border: 1px solid #ddd;
        }}
    """

    if alternate_rows:
        css_styles += """
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        """

    if hover_effect:
        css_styles += """
        tr:hover {
            background-color: #ddd;
        }
        """

    css_styles += """
    </style>
    """

    display(HTML(css_styles + html_table))


def display_table_with_stats(df, title=None, stats_cols=None, **kwargs):
    """
    Display a styled table with summary statistics below it.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to display.
    title : str, optional
        Title to display above the table.
    stats_cols : list of str, optional
        Columns to compute statistics for (must be numeric).
        If *None*, all numeric columns are used.
    **kwargs
        Forwarded to :func:`display_styled_table`.

    Examples
    --------
    >>> display_table_with_stats(df, title="Sales Summary")
    >>> display_table_with_stats(df, title="Sales Summary", stats_cols=["AIC", "Improvement"])
    """
    display_styled_table(df, title=title, **kwargs)

    if stats_cols is None:
        stats_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if stats_cols:
        print("\n" + "-" * 80)
        print("SUMMARY STATISTICS")
        print("-" * 80)

        stats_df = df[stats_cols].describe().round(4)
        display_styled_table(stats_df, header_color="#2196F3", font_size="10px")

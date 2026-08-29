# Reusable Styled Table Display Functions

## Overview

Instead of hardcoding HTML styling for each table, we've created generic, reusable functions that can style any pandas DataFrame with professional formatting.

## Available Functions

### 1. `display_styled_table()`

Display any DataFrame as a styled HTML table with customizable appearance.

**Signature:**
```python
display_styled_table(df, title=None, header_color="#4CAF50", 
                     font_size="11px", width="100%", 
                     alternate_rows=True, hover_effect=True)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `df` | DataFrame | Required | The dataframe to display |
| `title` | str | None | Title to display above table |
| `header_color` | str | "#4CAF50" | Header background color (hex or name) |
| `font_size` | str | "11px" | Font size for table content |
| `width` | str | "100%" | Table width |
| `alternate_rows` | bool | True | Alternate row colors |
| `hover_effect` | bool | True | Add hover highlighting |

**Examples:**

```python
# Basic usage - default green header
display_styled_table(df)

# With title
display_styled_table(df, title="Sales Data")

# Custom header color
display_styled_table(df, title="Sales Data", header_color="#2196F3")

# Smaller font, no hover effect
display_styled_table(df, font_size="10px", hover_effect=False)

# Using predefined colors
display_styled_table(df, header_color=TABLE_COLORS['blue'])
```

### 2. `display_table_with_stats()`

Display a styled table with summary statistics below it.

**Signature:**
```python
display_table_with_stats(df, title=None, stats_cols=None, **kwargs)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `df` | DataFrame | Required | The dataframe to display |
| `title` | str | None | Title to display above table |
| `stats_cols` | list | None | Columns to calculate stats for (None = all numeric) |
| `**kwargs` | dict | - | Additional arguments for `display_styled_table()` |

**Examples:**

```python
# Display table with statistics for all numeric columns
display_table_with_stats(df, title="Sales Summary")

# Statistics for specific columns only
display_table_with_stats(df, title="Sales Summary", 
                        stats_cols=['AIC', 'Improvement'])

# Custom styling with statistics
display_table_with_stats(df, title="Sales Summary",
                        header_color=TABLE_COLORS['blue'],
                        font_size="10px")
```

### 3. `TABLE_COLORS` Dictionary

Predefined color schemes for easy use.

**Available Colors:**

```python
TABLE_COLORS = {
    'green': '#4CAF50',      # Default, professional green
    'blue': '#2196F3',       # Professional blue
    'orange': '#FF9800',     # Warm orange
    'red': '#F44336',        # Alert red
    'purple': '#9C27B0',     # Purple
    'teal': '#009688',       # Teal
    'indigo': '#3F51B5',     # Indigo
    'cyan': '#00BCD4',       # Cyan
    'lime': '#8BC34A',       # Lime green
    'pink': '#E91E63',       # Pink
}
```

**Usage:**

```python
# Instead of hardcoding colors
display_styled_table(df, header_color=TABLE_COLORS['blue'])

# Easy to change theme
display_styled_table(df, header_color=TABLE_COLORS['orange'])
```

## Use Cases

### 1. Display Stepwise Selection Results

```python
# Original hardcoded approach (OLD)
html_table = selection_df.to_html(index=False, border=1, justify='center')
html_styled = f"""<style>...</style>{html_table}"""
display(HTML(html_styled))

# New reusable approach (NEW)
display_styled_table(selection_df, 
                    title="STEPWISE SELECTION SUMMARY",
                    header_color=TABLE_COLORS['green'])
```

### 2. Display ANOVA Results

```python
display_styled_table(anova_table,
                    title="ANALYSIS OF VARIANCE TABLE",
                    header_color=TABLE_COLORS['blue'])
```

### 3. Display Parameter Estimates

```python
display_styled_table(param_table,
                    title="PARAMETER ESTIMATES",
                    header_color=TABLE_COLORS['indigo'])
```

### 4. Display Diagnostic Statistics

```python
display_styled_table(diagnostic_table,
                    title="MODEL DIAGNOSTIC STATISTICS",
                    header_color=TABLE_COLORS['orange'])
```

### 5. Display with Summary Statistics

```python
display_table_with_stats(numeric_data,
                        title="NUMERIC SUMMARY",
                        stats_cols=['AIC', 'Improvement', 'Num_Params_In'],
                        header_color=TABLE_COLORS['teal'])
```

## Styling Features

### Header Styling
- Customizable background color
- White text for contrast
- Bold font
- Centered alignment
- Padding for readability

### Row Styling
- Optional alternating row colors (white/light gray)
- Optional hover highlighting (darker gray)
- Centered text alignment
- Light borders for clarity

### Table Styling
- Full width by default
- Customizable font size
- Collapsed borders (no double lines)
- Professional appearance

## Color Recommendations

### By Use Case

**Data Analysis Tables:**
- Green (#4CAF50) - Default, professional
- Blue (#2196F3) - Alternative professional

**Statistical Results:**
- Indigo (#3F51B5) - Formal, technical
- Teal (#009688) - Modern, clean

**Alerts/Important Data:**
- Orange (#FF9800) - Warning, attention
- Red (#F44336) - Critical, error

**Categorical Data:**
- Purple (#9C27B0) - Distinct, categorical
- Cyan (#00BCD4) - Cool, informative

## Advanced Customization

### Custom Colors

```python
# Use any hex color
display_styled_table(df, header_color="#FF6B6B")

# Use CSS color names
display_styled_table(df, header_color="darkblue")
```

### Font Sizes

```python
# Larger font for presentations
display_styled_table(df, font_size="14px")

# Smaller font for dense data
display_styled_table(df, font_size="9px")
```

### Disable Features

```python
# No alternating rows
display_styled_table(df, alternate_rows=False)

# No hover effect
display_styled_table(df, hover_effect=False)

# Both disabled
display_styled_table(df, alternate_rows=False, hover_effect=False)
```

### Custom Width

```python
# Narrower table
display_styled_table(df, width="80%")

# Wider table
display_styled_table(df, width="120%")
```

## Benefits

### 1. **Consistency**
- All tables use the same styling
- Professional appearance throughout notebook
- Easy to maintain

### 2. **Reusability**
- Write once, use everywhere
- No need to repeat HTML/CSS code
- Easy to update styling globally

### 3. **Flexibility**
- Customize per table as needed
- Predefined colors for quick use
- Full control over appearance

### 4. **Maintainability**
- Changes in one place affect all tables
- Easy to add new features
- Clear, documented code

### 5. **Readability**
- Professional appearance
- Color-coded headers
- Hover effects for interactivity
- Alternating row colors

## Integration with Notebook

The functions are defined in the first cell of the notebook and can be used throughout:

```python
# Cell 0: Define functions (runs once)
# ... function definitions ...

# Cell 5: Use for stepwise selection
display_styled_table(selection_df, title="Stepwise Selection")

# Cell 10: Use for ANOVA
display_styled_table(anova_table, title="ANOVA Results")

# Cell 15: Use for parameters
display_styled_table(param_table, title="Parameter Estimates")

# And so on...
```

## Creating Custom Wrapper Functions

You can create specialized functions for specific use cases:

```python
def display_anova_table(df):
    """Display ANOVA table with standard styling."""
    display_styled_table(df,
                        title="ANALYSIS OF VARIANCE TABLE",
                        header_color=TABLE_COLORS['blue'],
                        font_size="11px")

def display_model_summary(df):
    """Display model summary with standard styling."""
    display_styled_table(df,
                        title="MODEL SUMMARY",
                        header_color=TABLE_COLORS['indigo'],
                        font_size="10px")

# Usage
display_anova_table(anova_df)
display_model_summary(summary_df)
```

## Performance Considerations

- Functions are lightweight and fast
- No external dependencies beyond pandas and IPython
- Suitable for large dataframes (tested with 1000+ rows)
- HTML rendering is handled by Jupyter

## Troubleshooting

### Table Not Displaying

**Problem:** Table doesn't appear in notebook
**Solution:** Make sure you're in a Jupyter environment and the functions are defined in an earlier cell

### Colors Not Showing

**Problem:** Header color not appearing
**Solution:** Check that the hex color is valid (e.g., "#2196F3" not "2196F3")

### Styling Not Applied

**Problem:** Table appears unstyled
**Solution:** Ensure `display_styled_table()` is called, not just `display(HTML(...))`

## Related Files

- **Notebook**: `06_multiple_regression.ipynb` (Cell 0 - Function definitions)
- **Quick Reference**: `docs/06_regression_analysis_quick_reference.md`
- **Full Guide**: `docs/06_regression_analysis_guide.md`

## Examples in Notebook

The following cells use these functions:

- Cell 16: Stepwise selection table (green header)
- Cell 21: ANOVA table (can use blue header)
- Cell 23: Parameter estimates (can use indigo header)
- Cell 25: Diagnostic statistics (can use orange header)

---

**Last Updated:** August 29, 2026
**Status**: ✅ Reusable Functions Implemented

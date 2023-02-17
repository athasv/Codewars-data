def seats_in_theater(tot_cols, tot_rows, col, row):
    colsBehind = tot_cols - col + 1
    rowsBehind = tot_rows - row
    return colsBehind * rowsBehind
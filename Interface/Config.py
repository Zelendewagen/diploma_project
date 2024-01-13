
# Вычисление "Х" координаты
def x_pos(window, width):
    return (window.winfo_screenwidth() - width) // 2


# Вычисление "У" координаты
def y_pos(window, height):
    return (window.winfo_screenheight() - height) // 2


# Определение центрального положения окна
def window_geometry(window, width, height):
    return (f"{width}x{height}+{x_pos(window, width)}"
            f"+{y_pos(window, height)}")


main_window_width = 500
main_window_height = 260

top_window_width = 350
top_window_height = 120





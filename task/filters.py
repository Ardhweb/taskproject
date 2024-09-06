from .models import Task




def filter_list(status=None, sort_by=None):
    """
    Filters and sorts tasks based on the provided status, sorting option, and priority level.

    Args:
        status (str, optional): The status to filter tasks by (e.g., 'To Do', 'In Progress', 'Done'). Defaults to None.
        sort_by (str, optional): The field to sort tasks by (e.g., 'priority', 'due_date'). Defaults to None.
        priority_level (str, optional): The priority level to filter tasks by if 'priority' is selected as the sort option. Defaults to None.

    Returns:
        QuerySet: A QuerySet of tasks filtered and sorted based on the provided criteria.
    """
    
    # If both status and sort_by are provided, and sort_by is 'priority', filter by both status and priority level.
    if status and sort_by:
        tasks = Task.objects.filter(status=status).order_by(sort_by)
    # If only status is provided, filter tasks by the given status.
    elif status:
        tasks = Task.objects.filter(status=status)
    # If only sort_by is provided, order tasks by the given sort field.
    elif sort_by:
        tasks = Task.objects.order_by(sort_by)
    # If neither status nor sort_by is provided, return all tasks.
    else:
        tasks = Task.objects.all()

    return tasks

    

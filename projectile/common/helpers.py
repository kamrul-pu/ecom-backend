def pk_extractor(queryset):
    """
    this method return  pk of every item of a queryset as list
    """
    instances_pk = []
    for item in queryset:
        if isinstance(item, int):
            instances_pk.append(item)
        else:
            instances_pk.append(item.id)
    return instances_pk

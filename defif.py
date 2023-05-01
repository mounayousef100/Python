def names(ahmad,hasan,ali):
    if ahmad> hasan and ahmad > ali:
        return ahmad
    elif hasan> ahmad and hasan > ali:
        return hasan
    else:
        return ali
print(names(70, 33, 80))

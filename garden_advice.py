def get_user_input():
    season = input("Enter the season (summer / winter): ").strip().lower()
    plant_type = input("Enter the plant type (flower / vegetable): ").strip().lower()
    return season, plant_type

def get_advice(season, plant_type):
    advice = ""
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    return advice

def main():
    season, plant_type = get_user_input()
    advice = get_advice(season, plant_type)
    print(advice)

if __name__ == "__main__":
    main()
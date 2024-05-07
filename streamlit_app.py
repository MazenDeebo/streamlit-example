def main():
    print("Career Assessment")
    print("Please fill this form carefully and precisely because this data will be used for career analysis.")

    full_name = input('Full Name: ')

    major_options = ('Engineering (هندسة)', 'Medical (طب)', 'Computer Science (حاسبات و معلومات)', 'Sport Science (تربية رياضية)', 'Business (تجارة)')
    print("Major (your college):")
    for idx, option in enumerate(major_options, 1):
        print(f"{idx}. {option}")
    major_idx = int(input("Enter the number corresponding to your major: "))
    major = major_options[major_idx - 1]

    activities_options = [
        'Adapt to change or perform a variety of duties that may change',
        'Budget and handle money and records with accuracy and reliability',
        'Care about people, their needs, and their problems',
        'Concentrate for long periods without being distracted',
        'Do routine, organized, and accurate work',
        'Explore new technology',
        'Find the best way or a new way to do something',
        'Help people overcome their challenges to be at their best',
        'Have a flexible schedule',
        'Handle several responsibilities at once'
    ]
    print("Activities (Choose one or more):")
    for idx, option in enumerate(activities_options, 1):
        print(f"{idx}. {option}")
    activities_indices = input("Enter the numbers corresponding to your activities separated by commas (e.g., 1,3,5): ")
    activities = [activities_options[int(idx) - 1] for idx in activities_indices.split(',')]

    character_options = [
        'Adventurous',
        'Caring',
        'Competitive',
        'Creative and imaginative',
        'Creative problem-solver',
        'Decision maker',
        'Friendly',
        'Good communicator'
    ]
    print("What would describe you? (Choose one or more):")
    for idx, option in enumerate(character_options, 1):
        print(f"{idx}. {option}")
    character_indices = input("Enter the numbers corresponding to your character traits separated by commas (e.g., 1,3,5): ")
    character_traits = [character_options[int(idx) - 1] for idx in character_indices.split(',')]

    personal_traits_options = [
        'Non-judgmental',
        'Non-materialistic',
        'Optimistic',
        'Organized',
        'Pay attention to detail',
        'Persuasive',
        'Problem solver',
        'Self-confident',
        'See details in the big picture'
    ]
    print("(Choose one or more) personal traits:")
    for idx, option in enumerate(personal_traits_options, 1):
        print(f"{idx}. {option}")
    personal_indices = input("Enter the numbers corresponding to your personal traits separated by commas (e.g., 1,3,5): ")
    personal_traits = [personal_traits_options[int(idx) - 1] for idx in personal_indices.split(',')]

    stressed_out = input('I get stressed out easily (Yes/No): ')

    favorite_subjects_options = [
        'Biology',
        'Chemistry',
        'Computer',
        'Physics',
        'Math',
        'Foreign Language',
        'Geography',
        'History'
    ]
    print("Favorite School Subjects (Choose one or more):")
    for idx, option in enumerate(favorite_subjects_options, 1):
        print(f"{idx}. {option}")
    favorite_subjects_indices = input("Enter the numbers corresponding to your favorite subjects separated by commas (e.g., 1,3,5): ")
    favorite_subjects = [favorite_subjects_options[int(idx) - 1] for idx in favorite_subjects_indices.split(',')]

    # Perform prediction or data processing here based on the collected inputs
    print("Prediction:")
    print(f"Full Name: {full_name}")
    print(f"Major: {major}")
    print(f"Activities: {', '.join(activities)}")
    print(f"Character Traits: {', '.join(character_traits)}")
    print(f"Personal Traits: {', '.join(personal_traits)}")
    print(f"Stressed Out: {stressed_out}")
    print(f"Favorite Subjects: {', '.join(favorite_subjects)}")

if __name__ == "__main__":
    main()

from behave import given, when, then

@given(u'I put {thing} in a blender,')
def step_impl(context, thing):
    context.selected_thing = thing

@when(u'I switch the blender on')
def step_impl(context):
    if context.selected_thing == "ice":
        context.transformed_thing = "crushed ice"
    elif context.selected_thing == "avocado":
        context.transformed_thing = "not guacamole"
    print("----------Blender started with ", context.selected_thing)

@then(u'it should transform into {other_thing}')
def step_impl(context, other_thing):
    assert(other_thing == context.transformed_thing)
